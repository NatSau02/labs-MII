package server

import (
	"task2/internal/app/shelf_for_books/models"
	"task2/internal/app/shelf_for_books/repository"
)

type ShelfService struct {
repo repository.ShelfBooks
}

func NewShelfService(repo repository.ShelfBooks) *ShelfService {
	return &ShelfService{repo: repo}
}

func (s *ShelfService) CreateShelf(model *models.Shelf) (int, error) {
	return s.repo.Create(model)
}
func (s *ShelfService) GetAll() ([]models.ShelfList, error){
	return s.repo.GetAll()
}