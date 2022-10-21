package server

import (
	"context"
	"net/http"
	"time"
)

type Srv struct {
	httpServer *http.Server
}

func (s *Srv) Run(port string,router http.Handler) error { //,
	s.httpServer = &http.Server{
		Addr:           ":" + port,
		Handler:        router,
		MaxHeaderBytes: 1 << 20, // 1 MB
		ReadTimeout:    10 * time.Second,
		WriteTimeout:   10 * time.Second,
	}

	return s.httpServer.ListenAndServe()
}
func (s *Srv) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	s.httpServer.Handler.ServeHTTP(w, r)

}
func (s *Srv) Shutdown(ctx context.Context) error {
	return s.httpServer.Shutdown(ctx)
}