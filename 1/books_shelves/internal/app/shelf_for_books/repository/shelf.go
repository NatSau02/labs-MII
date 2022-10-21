package repository

import (
	"github.com/jmoiron/sqlx"
	"task2/internal/app/shelf_for_books/models"
)

type ShelfBooksPostgres struct {
	db *sqlx.DB
}

func NewShelfBooksPostgres(db *sqlx.DB) *ShelfBooksPostgres {
	return &ShelfBooksPostgres{db: db}
}

func (s *ShelfBooksPostgres) Create(item *models.Shelf) (int, error) {
	tx := s.db.MustBegin()
	defer tx.Rollback()
	var id int
	createListQuery :=`INSERT INTO public.shelf (shelf_gerne) VALUES ($1) RETURNING id_shelf`
	row := tx.QueryRow(createListQuery, item.Id_Gerne)
	if err := row.Scan(&id); err != nil {
		return 0, err
	}
    for i:=range item.Books{
		item.Books[i].Book_Shelf=id
	}
	_, err := tx.NamedExec(`INSERT INTO public.book (author,name,status,book_shelf) VALUES (:author,:name,:status,:book_shelf)`, item.Books)
	if err != nil {
		return 0, err
	}
	return id, tx.Commit()
}
func (s *ShelfBooksPostgres) GetAll() ([]models.ShelfList, error) {
	var list []models.ShelfList
	listQuery := `select shelf.id_shelf,gerne.id_gerne,gerne.name as name_g, ` +
		`array_agg(book.name) as book ` +
		`from gerne join shelf on gerne.id_gerne=shelf.shelf_gerne join book ` +
		`ON shelf.id_shelf=book.book_shelf group by (shelf.id_shelf,gerne.id_gerne)`

	err := s.db.Select(&list, listQuery)
	return list, err
}
	// //вариант со страндартной библиотекой
	////rows, err :=  s.db.Query( listQuery )
	////if err != nil {
	////	panic(err)
	////}
	////defer rows.Close()
	////
	////for rows.Next(){
	////	var item models.ShelfList
	////	err := rows.Scan(&item.Id_Shelf,&item.Shelf_Gerne,&item.Book)
	////	if err != nil{
	////		fmt.Println(err)
	////		continue
	////	}
	////	list = append(list,item)
	////}
	////return list, err
