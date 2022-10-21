package handler

import (
	"context"
	"encoding/json"
	"github.com/gorilla/mux"
	"math/rand"
	"net/http"
	"strconv"
	"task2/internal/app/shelf_for_books/server"
)
const (
	ctxKeyRequestID=iota
)
type Handler struct {
	services *server.Server
}
type statusResponse struct {
	Status string `json:"status"`
}
func NewHandler(services *server.Server) *Handler {
	return &Handler{services: services}
}

func (h *Handler) InitRoutes() *mux.Router {
	router := mux.NewRouter()
	router.Use(h.setRequestID)
	router.HandleFunc("/book", h.handleBookCreate()).Methods("POST")
	router.HandleFunc("/book/{id:[0-9]+}", h.handleBookFindById()).Methods("GET")
	router.HandleFunc("/book/all", h.handleBookAll()).Methods("GET")
	router.HandleFunc("/shelf/all", h.handleShelfAll()).Methods("GET")
	router.HandleFunc("/shelf", h.handleShelfCreate()).Methods("POST")

	return router
}
func (h *Handler) setRequestID(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		id := strconv.Itoa((rand.Intn(100)+10)*100)
		w.Header().Set("X-Request-ID", id)
		next.ServeHTTP(w, r.WithContext(context.WithValue(r.Context(), ctxKeyRequestID, id)))
	})
}
func (h *Handler) Error(w http.ResponseWriter, r *http.Request, code int, err error) {
	h.Respond(w, r, code, map[string]string{"error": err.Error()})
}

func (h *Handler) Respond(w http.ResponseWriter, r *http.Request, code int, data interface{}) {
	w.WriteHeader(code)
	if data != nil {
		json.NewEncoder(w).Encode(data)
	}
}