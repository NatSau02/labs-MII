package main

import
(
	"context"
	"github.com/sirupsen/logrus"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"task2/internal/app/shelf_for_books/handler"
	repository2 "task2/internal/app/shelf_for_books/repository"
	server2 "task2/internal/app/shelf_for_books/server"
)

func main()  {

	db, err := repository2.NewPostgresDB(repository2.Config{
		Username: "postgres",
		DBName:   "postgres",
		SSLMode:  "disable",
		Password: "qwerty",
	})
	if err != nil {
		logrus.Fatalf("failed to initialize db: %s", err.Error())
	}
	repos := repository2.NewRepository(db)
	services := server2.NewServer(repos)
	handlers := handler.NewHandler(services)

	srv := new(server2.Srv)
	go func() {
		if err := srv.Run("8000",handlers.InitRoutes()); err != http.ErrServerClosed{
			logrus.Fatalf("error occured while running http server: %s", err.Error())
		}
	}()

	logrus.Print("App Started")

	quit := make(chan os.Signal, 1)
	signal.Notify(quit, syscall.SIGTERM, syscall.SIGINT)
	<-quit

	logrus.Print("App Shutting Down")

	if err := srv.Shutdown(context.Background()); err != nil {
		logrus.Errorf("error occured on server shutting down: %s", err.Error())
	}

	if err := db.Close(); err != nil {
		logrus.Errorf("error occured on db connection close: %s", err.Error())
	}
}
