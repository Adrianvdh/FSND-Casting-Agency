--
-- PostgreSQL database dump
--

-- Dumped from database version 12.6
-- Dumped by pg_dump version 12.6

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

--
-- Name: gender; Type: TYPE; Schema: public; Owner: adrian
--

CREATE TYPE public.gender AS ENUM (
    'Male',
    'Female'
);


ALTER TYPE public.gender OWNER TO adrian;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Actor; Type: TABLE; Schema: public; Owner: adrian
--

CREATE TABLE public."Actor" (
    id integer NOT NULL,
    full_name character varying(120),
    description character varying(500),
    date_of_birth date,
    height integer,
    gender public.gender,
    cover_image_url character varying(500)
);


ALTER TABLE public."Actor" OWNER TO adrian;

--
-- Name: Actor_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE public."Actor_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Actor_id_seq" OWNER TO adrian;

--
-- Name: Actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE public."Actor_id_seq" OWNED BY public."Actor".id;


--
-- Name: Cast; Type: TABLE; Schema: public; Owner: adrian
--

CREATE TABLE public."Cast" (
    movie_id integer NOT NULL,
    actor_id integer NOT NULL
);


ALTER TABLE public."Cast" OWNER TO adrian;

--
-- Name: Genre; Type: TABLE; Schema: public; Owner: adrian
--

CREATE TABLE public."Genre" (
    id integer NOT NULL,
    name character varying(120)
);


ALTER TABLE public."Genre" OWNER TO adrian;

--
-- Name: Genre_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE public."Genre_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Genre_id_seq" OWNER TO adrian;

--
-- Name: Genre_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE public."Genre_id_seq" OWNED BY public."Genre".id;


--
-- Name: Movie; Type: TABLE; Schema: public; Owner: adrian
--

CREATE TABLE public."Movie" (
    id integer NOT NULL,
    title character varying(120),
    description character varying(500),
    genre_id integer,
    release_date date,
    duration integer,
    cover_image_url character varying(500)
);


ALTER TABLE public."Movie" OWNER TO adrian;

--
-- Name: Movie_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE public."Movie_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Movie_id_seq" OWNER TO adrian;

--
-- Name: Movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE public."Movie_id_seq" OWNED BY public."Movie".id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: adrian
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO adrian;

--
-- Name: Actor id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY public."Actor" ALTER COLUMN id SET DEFAULT nextval('public."Actor_id_seq"'::regclass);


--
-- Name: Genre id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY public."Genre" ALTER COLUMN id SET DEFAULT nextval('public."Genre_id_seq"'::regclass);


--
-- Name: Movie id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY public."Movie" ALTER COLUMN id SET DEFAULT nextval('public."Movie_id_seq"'::regclass);


--
-- Data for Name: Actor; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY public."Actor" (id, full_name, description, date_of_birth, height, gender, cover_image_url) FROM stdin;
29	Meg Ryan	Meg Ryan is an American actress and producer. Ryan began her acting career in 1981 in minor roles before joining the cast of the CBS soap opera As the World Turns in 1982.	1961-11-19	173	Female	https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRaylUHDnhsws_8SY-iV2eAnrsR9d3hAtkELLjBz9JDA_LFSN_b
30	Billy Crystal	William Edward Crystal is an American actor, comedian, writer, producer, director and television host. He gained prominence in the 1970s and 1980s for television roles as Jodie Dallas on the ABC sitcom Soap and as a cast member and frequent host of Saturday Night Live	1948-03-14	170	Male	https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTC8rNntc8fBOn3susRUeFJTJDOkt_0Y30znA0BOci132r75MKy
31	Carrie Fisher	Carrie Frances Fisher was an American actress and writer. Fisher played Princess Leia in the Star Wars films, a role for which she was nominated for four Saturn Awards. Her other film credits include Shampoo, The Blues Brothers, Hannah and Her Sisters, The 'Burbs, When Harry Met Sally..., Soapdish, and The Women.	1956-10-21	0	Female	https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR9PvSl232PSP3qMJe63g7hiIGb_kjzXiWaugTQMVhRmVc-G5fK
32	Bruno Kirby	Bruno Kirby was an American actor, singer, voice artist, and comedian. He was known for his roles in City Slickers, When Harry Met Sally..., Good Morning, Vietnam, The Godfather Part II, and Donnie Brasco. He voiced Reginald Stout in Stuart Little.	1949-04-28	169	Male	https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZK_aGnd1o2zh0bAm-FzABkT1OMaaqXSyaUvTX-q2pboROW63w
33	Nora Ephron	Nora Ephron was an American journalist, writer, and filmmaker. She is best known for her romantic comedy films and was nominated three times for the Academy Award for Best Writing: for Silkwood, When Harry Met Sally..., and Sleepless in Seattle.	1941-06-19	0	Female	https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQgphFZT5J2LQXw_zQl86ztFKuSFgxeNF2TqxJQNXlLb4q9udzL
\.


--
-- Data for Name: Cast; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY public."Cast" (movie_id, actor_id) FROM stdin;
74	29
74	30
74	31
74	32
74	33
\.


--
-- Data for Name: Genre; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY public."Genre" (id, name) FROM stdin;
1	Kids
33	Fantasy/Sci-fi
34	Thriller/Romance
35	Musical/Family
36	Kids
37	Romance/Comedy
\.


--
-- Data for Name: Movie; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY public."Movie" (id, title, description, genre_id, release_date, duration, cover_image_url) FROM stdin;
74	When Harry Met Sally...	A chance encounter between two graduates culminates in a short-term friendship. But when fate brings them back together five years later, they are forced to deal with how they feel about each other.	37	1989-07-21	96	https://m.media-amazon.com/images/M/MV5BMjE0ODEwNjM2NF5BMl5BanBnXkFtZTcwMjU2Mzg3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY public.alembic_version (version_num) FROM stdin;
2751932a6eab
\.


--
-- Name: Actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('public."Actor_id_seq"', 38, true);


--
-- Name: Genre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('public."Genre_id_seq"', 37, true);


--
-- Name: Movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('public."Movie_id_seq"', 74, true);


--
-- Name: Actor Actor_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY public."Actor"
    ADD CONSTRAINT "Actor_pkey" PRIMARY KEY (id);


--
-- Name: Cast Cast_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY public."Cast"
    ADD CONSTRAINT "Cast_pkey" PRIMARY KEY (movie_id, actor_id);


--
-- Name: Genre Genre_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY public."Genre"
    ADD CONSTRAINT "Genre_pkey" PRIMARY KEY (id);


--
-- Name: Movie Movie_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY public."Movie"
    ADD CONSTRAINT "Movie_pkey" PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: Cast Cast_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY public."Cast"
    ADD CONSTRAINT "Cast_actor_id_fkey" FOREIGN KEY (actor_id) REFERENCES public."Actor"(id);


--
-- Name: Cast Cast_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY public."Cast"
    ADD CONSTRAINT "Cast_movie_id_fkey" FOREIGN KEY (movie_id) REFERENCES public."Movie"(id);


--
-- Name: Movie Movie_genre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY public."Movie"
    ADD CONSTRAINT "Movie_genre_id_fkey" FOREIGN KEY (genre_id) REFERENCES public."Genre"(id);


--
-- PostgreSQL database dump complete
--

