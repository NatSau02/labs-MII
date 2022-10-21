package models

import "github.com/lib/pq"

type ShelfList struct{
	Id_Shelf int  `json:"id_shelf"`
	//Shelf_Gerne int    `json:"shelf_gerne"`
	Gerne `json:"shelf_gerne"`
//	Book  `json:"books"`
	Book pq.StringArray `json:"books"`
}
type Shelf struct{
	Id_Shelf int  `json:"id_shelf"`
	Gerne    `json:"shelf_gerne"`
	Books    []Book `json:"books"`
}
type Shelf2 struct{
	Id_Shelf int  `json:"id_shelf"`
	Gerne    `json:"shelf_gerne"`
	Books    []Book `json:"books"`
}
type Gerne struct {
	Id_Gerne int  `json:"id_gerne"`
	Name_G string  `json:"name_g"`
}
type Book struct {
	Id_Book int `json:"id_book"`
	Author string `json:"author"`
	Name string  `json:"name"`
	Status bool  `json:"status"`
	Book_Shelf int  `json:"book_shelf"`
}
