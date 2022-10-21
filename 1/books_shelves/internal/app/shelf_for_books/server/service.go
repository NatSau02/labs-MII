package server

import (
	"task2/internal/app/shelf_for_books/models"
	"task2/internal/app/shelf_for_books/repository"
)

type Books interface {
	Create(model *models.Book) (error)
	FindById(id int)(models.Book, error)
	FindAll()([]models.Book, error)
}
type Shelf interface {
	CreateShelf(model *models.Shelf) (int, error)
	GetAll() ([]models.ShelfList, error)
}
type Server struct {
	Books
	Shelf
}
func NewServer(repos *repository.Repository) *Server {
	return &Server{
		Books: NewBookService(repos.Book),
		Shelf: NewShelfService(repos.ShelfBooks),
	}
}
