CREATE DATABASE asyncio_example
WITH ENCODING='UTF8'
CONNECTION LIMIT=-1;


CREATE TABLE public.animal (
   id serial NOT NULL,
   name character varying(30) NOT NULL,
   age smallint NOT NULL,
   CONSTRAINT pk_animal PRIMARY KEY (id)
) WITH (
  OIDS = FALSE
);

INSERT INTO public.animal(name, age) VALUES('Bruno', 9);
INSERT INTO public.animal(name, age) values('Max', 3);