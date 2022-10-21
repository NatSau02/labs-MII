package repository

import (
	"github.com/jmoiron/sqlx"
	"task2/internal/app/shelf_for_books/models"
)

type BookPostgres struct {
	db *sqlx.DB
}

func NewBookPostgres(db *sqlx.DB) *BookPostgres {
	return &BookPostgres{db: db}
}

func (r *BookPostgres) Create(m *models.Book) (error) {
	_, err := r.db.NamedExec(`INSERT INTO public.book (author,name,status,book_shelf) VALUES (:author,:name,:status,:book_shelf)`, m)
	if err != nil {
		return err
	}
	return err
}
func (r *BookPostgres) FindById(id int) (models.Book,error) {
	var mod models.Book

	queryNew := `SELECT id_book,author,name,status,book_shelf FROM public.book WHERE id_book = $1`
	row := r.db.QueryRow(queryNew, id)
	err := row.Scan(&mod.Id_Book,&mod.Author,&mod.Name,&mod.Status,&mod.Book_Shelf)
	if err != nil {
		return mod, err
	}
	return mod, err
}
func (r *BookPostgres) FindAll() ([]models.Book,error) {
	var mod []models.Book
	queryNew := `SELECT id_book,author,name,status,book_shelf FROM public.book`
	err := r.db.Select(&mod,queryNew)
	return mod, err
}
