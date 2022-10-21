package handler

import (
	"encoding/json"
	"net/http"
	"task2/internal/app/shelf_for_books/models"
)

func (h *Handler) handleShelfCreate() http.HandlerFunc {

	return func(w http.ResponseWriter, r *http.Request) {
		req := &models.Shelf{}
		if err := json.NewDecoder(r.Body).Decode(req); err != nil {
			h.Error(w, r, http.StatusBadRequest, err)
			return
		}

		id, err := h.services.CreateShelf(req);
		if err != nil {
			h.Error(w, r, http.StatusUnprocessableEntity, err)
			return
		}

		h.Respond(w, r, http.StatusCreated, id)
	}
}
func (h *Handler) handleShelfAll() http.HandlerFunc {

	return func(w http.ResponseWriter, r *http.Request) {

		list, err := h.services.GetAll();
		if err != nil {
			h.Error(w, r, http.StatusUnprocessableEntity, err)
			return
		}

		h.Respond(w, r, http.StatusOK, list)


	}
}
