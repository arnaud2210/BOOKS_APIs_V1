--
-- PostgreSQL database dump
--

-- Dumped from database version 11.14
-- Dumped by pg_dump version 11.14

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: books; Type: TABLE; Schema: public; Owner: naud
--

CREATE TABLE public.books (
    id_book integer NOT NULL,
    isbn character varying(12) NOT NULL,
    titre character varying(200) NOT NULL,
    date_publication character varying(10) NOT NULL,
    auteur character varying(200) NOT NULL,
    editeur character varying(150) NOT NULL,
    categorie_id integer NOT NULL
);


ALTER TABLE public.books OWNER TO naud;

--
-- Name: books_id_book_seq; Type: SEQUENCE; Schema: public; Owner: naud
--

CREATE SEQUENCE public.books_id_book_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.books_id_book_seq OWNER TO naud;

--
-- Name: books_id_book_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: naud
--

ALTER SEQUENCE public.books_id_book_seq OWNED BY public.books.id_book;


--
-- Name: categories; Type: TABLE; Schema: public; Owner: naud
--

CREATE TABLE public.categories (
    id_cat integer NOT NULL,
    libelle_categorie character varying(50)
);


ALTER TABLE public.categories OWNER TO naud;

--
-- Name: categories_id_cat_seq; Type: SEQUENCE; Schema: public; Owner: naud
--

CREATE SEQUENCE public.categories_id_cat_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_cat_seq OWNER TO naud;

--
-- Name: categories_id_cat_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: naud
--

ALTER SEQUENCE public.categories_id_cat_seq OWNED BY public.categories.id_cat;


--
-- Name: books id_book; Type: DEFAULT; Schema: public; Owner: naud
--

ALTER TABLE ONLY public.books ALTER COLUMN id_book SET DEFAULT nextval('public.books_id_book_seq'::regclass);


--
-- Name: categories id_cat; Type: DEFAULT; Schema: public; Owner: naud
--

ALTER TABLE ONLY public.categories ALTER COLUMN id_cat SET DEFAULT nextval('public.categories_id_cat_seq'::regclass);


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: naud
--

COPY public.books (id_book, isbn, titre, date_publication, auteur, editeur, categorie_id) FROM stdin;
1	978-2-3301-4	L'économie symbiotique: Régénérer la planète,l'économie,la société	Août 2021	Isabelle Delannoy	Actes Sud	7
2	978-2-7110-3	Code numérique 2020	Août 2021	Fabrices Mattatia	LexisNexis	7
3	978-2-3480-6	Economie de la dette	Oct. 2021	Anton Brender,Florence Pisani	La Découverte	7
4	978-2-8977-6	La recette parfaite: Mealprep végane	25-01-2022	Katia Bricka	Modus Vivendi	4
5	978-2-2631-2	Mon cahier Rituels zéro sucre	Janv. 2022	Marie-laure André	Solar	4
6	978-2-3480-6	Savoir quoi manger:Régime méditerranéen	25-01-2022	Nathalie Verret	Modus Vivendi	4
7	978-2-7491-7	La Cuisine de l'oasis	Nov. 2021	Patrick El Ouarghi, Philip Chapelet	Cherche Midi	4
8	978-2-3794-3	Les routes des épices	Oct. 2022	Hisanobu Shigeta	DUCASSE EDITION	4
9	978-2-4120-4	100 idées pour foutre la merde au bureau	Déc. 2021	Topito	First	5
10	978-2-4120-0	100 idées pour foutre de la merde à un dîner de famille	Déc. 2021	Topito	First	5
11	978-2-4512-8	Word 2021 pour les Nuls,grand format	13-01-2022	Dan Gookin	First Interactive	8
12	978-2-3260-0	Architecture logicielle propre	Nov. 2020	Robert C. Martin	Pearson	8
13	979-2-5362-5	Les réseaux sociaux	Oct. 2020	Julie Lardon,Marie-Anne Wachnicki	Poule Qui Pond	8
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: naud
--

COPY public.categories (id_cat, libelle_categorie) FROM stdin;
1	Litterature
2	Histoire
3	Bandes dessinées
4	Cuisine
5	Humour
6	Tourisme et voyage
7	Droit et Economie
8	Informatique et internet
9	Sciences sociales
10	Essais et documents
11	Sports et Loisirs
\.


--
-- Name: books_id_book_seq; Type: SEQUENCE SET; Schema: public; Owner: naud
--

SELECT pg_catalog.setval('public.books_id_book_seq', 13, true);


--
-- Name: categories_id_cat_seq; Type: SEQUENCE SET; Schema: public; Owner: naud
--

SELECT pg_catalog.setval('public.categories_id_cat_seq', 11, true);


--
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: naud
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id_book);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: naud
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id_cat);


--
-- Name: books books_categorie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: naud
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_categorie_id_fkey FOREIGN KEY (categorie_id) REFERENCES public.categories(id_cat);


--
-- PostgreSQL database dump complete
--

