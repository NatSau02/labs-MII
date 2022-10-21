package handler

import (
	"encoding/json"
	"github.com/gorilla/mux"
	"net/http"
	"strconv"
	"task2/internal/app/shelf_for_books/models"
)

func (h *Handler) handleBookCreate() http.HandlerFunc {

	return func(w http.ResponseWriter, r *http.Request) {
		req := &models.Book{}
		if err := json.NewDecoder(r.Body).Decode(req); err != nil {
			h.Error(w, r, http.StatusBadRequest, err)
			return
		}

		err := h.services.Create(req);
		if err != nil {
			h.Error(w, r, http.StatusUnprocessableEntity, err)
			return
		}

		h.Respond(w, r, http.StatusCreated, statusResponse{"ok"})
	}
}
func (h *Handler) handleBookFindById() http.HandlerFunc {

	return func(w http.ResponseWriter, r *http.Request) {
		vars := mux.Vars(r)
		value,err := strconv.Atoi(vars["id"])
		if err !=nil{
			h.Error(w, r, http.StatusBadRequest, err)
			return
		}
		model, err := h.services.FindById(value);
		if err != nil {
			h.Error(w, r, http.StatusUnprocessableEntity, err)
			return
		}

		h.Respond(w, r, http.StatusOK, model)
	}
}
func (h *Handler) handleBookAll() http.HandlerFunc {

	return func(w http.ResponseWriter, r *http.Request) {


		model, err := h.services.FindAll();
		if err != nil {
			h.Error(w, r, http.StatusUnprocessableEntity, err)
			return
		}

		h.Respond(w, r, http.StatusOK, model)
	}
}