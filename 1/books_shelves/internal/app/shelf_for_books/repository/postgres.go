package repository

import (
	"fmt"
	"github.com/jmoiron/sqlx"
)

type Config struct {
	//Host     string
	//Port     string
	Username string
	Password string
	DBName   string
	SSLMode  string
}

func NewPostgresDB(cfg Config) (*sqlx.DB, error) {
	db, err := sqlx.Open("postgres", fmt.Sprintf("user=%s dbname=%s password=%s sslmode=%s", cfg.Username, cfg.DBName, cfg.Password, cfg.SSLMode))
	if err != nil {
		return nil, err
	}
    //defer db.Close()
	err = db.Ping()
	if err != nil {
		return nil, err
	}

	return db, nil
}

