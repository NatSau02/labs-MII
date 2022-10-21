package repository

import (
	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
	"task2/internal/app/shelf_for_books/models"
)


type ShelfBooks interface {
	Create(model *models.Shelf) (int, error)
	GetAll() ([]models.ShelfList, error)
}
type Book interface {
	Create(model *models.Book) (error)
	FindById(id int)(models.Book, error)
	FindAll()([]models.Book, error)
}

type Repository struct {
	ShelfBooks
	Book
}

func NewRepository(db *sqlx.DB) *Repository {
	return &Repository{

		ShelfBooks: NewShelfBooksPostgres(db),
		Book:       NewBookPostgres(db),
	}
}
