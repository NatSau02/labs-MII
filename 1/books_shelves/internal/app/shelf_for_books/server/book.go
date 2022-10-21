package server

import (
	"task2/internal/app/shelf_for_books/models"
	"task2/internal/app/shelf_for_books/repository"
)

type BookService struct {
	repo repository.Book
}

func NewBookService(repo repository.Book) *BookService {
	return &BookService{repo: repo}
}
func (s *BookService) Create(model *models.Book) (error){
	return s.repo.Create(model)
}
func (s *BookService) FindById(id int)(models.Book, error){
	return s.repo.FindById(id)
}
func (s *BookService) FindAll() ([]models.Book,error){
	return s.repo.FindAll()
}
