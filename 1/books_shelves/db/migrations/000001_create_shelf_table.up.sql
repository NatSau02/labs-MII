CREATE TABLE IF NOT EXISTS "gerne"(
   "id_gerne" serial PRIMARY KEY,
   "name" VARCHAR (100) NOT NULL
    );
CREATE TABLE IF NOT EXISTS "shelf"(
  "id_shelf" serial PRIMARY KEY,
  "shelf_gerne" INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS "book"(
  "id_book" serial PRIMARY KEY,
  "author" VARCHAR (100) NOT NULL,
  "name" VARCHAR (100) NOT NULL,
  "status" BOOLEAN NOT NULL,
  "book_shelf" INTEGER NOT NULL
 );
ALTER TABLE "shelf" ADD CONSTRAINT "uniq_shelf_gerne" UNIQUE ("shelf_gerne");

ALTER TABLE "shelf" ADD FOREIGN KEY ("shelf_gerne") REFERENCES "gerne" ("id_gerne")  ON DELETE CASCADE;

ALTER TABLE "book" ADD FOREIGN KEY ("book_shelf") REFERENCES "shelf" ("id_shelf")  ON DELETE CASCADE;

INSERT INTO "gerne" ("name")
VALUES ('роман'),
       ('практическая психология'),
       ('детектив');

INSERT INTO "shelf" ("shelf_gerne")
SELECT "id_gerne" FROM "gerne" WHERE "name"='роман';

INSERT INTO "shelf" ("shelf_gerne")
SELECT "id_gerne" FROM "gerne" WHERE "name"='практическая психология';

INSERT INTO "book" ("author", "name", "status","book_shelf")
SELECT 'Майн Рид', 'Всадник без головы', true, "id_shelf" FROM "shelf" JOIN "gerne" ON shelf.shelf_gerne=gerne.id_gerne AND gerne.name='роман';

INSERT INTO "book" ("author", "name", "status","book_shelf")
SELECT 'Тургенев', 'Накануне', false, "id_shelf" FROM "shelf" JOIN "gerne" ON shelf.shelf_gerne=gerne.id_gerne AND gerne.name='роман';

INSERT INTO "book" ("author", "name", "status","book_shelf")
SELECT 'Гончаров', 'Обрыв', true, "id_shelf" FROM "shelf" JOIN "gerne" ON shelf.shelf_gerne=gerne.id_gerne AND gerne.name='роман';

INSERT INTO "book" ("author", "name", "status","book_shelf")
SELECT 'Джордан Питерсон', '12 правил жизни', true, "id_shelf" FROM "shelf" JOIN "gerne" ON shelf.shelf_gerne=gerne.id_gerne AND gerne.name='практическая психология';



