create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------


-- non_parents is an optional, but recommended question
-- Q5: All non-parent relations ordered by height difference
create table non_parents as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

-- Q6: 
create table divisors as
	select a.n as x, count(b.n) as y
    from ints as a, ints as b
    where a.n %b.n = 0
    group by a.n;


--Q7:
create table primes as
    select x
    from divisors
    where y = 2;


/*DONE*/


-- Q1: The size of each dog
create table size_of_dogs as
  select d.name, s.size
  from dogs as d, sizes as s
  where d.height > s.min and d.height <= s.max;


-- Q2: All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select p.child
  from dogs as d, parents as p
  where p.parent = d.name  
  order by -d.height;


 -- Q3: Sentences about siblings that are the same size
create table sentences as
	with child (name, parent, size) as(
		select p.child, p.parent, s.size
			from parents as p, dogs as d, sizes as s
			where p.child = d.name and d.height > s.min and d.height <= s.max
 	)
  	select c1.name || " and " || c2.name || " are " || c1.size || " siblings"
  		from child as c1, child as c2
  		where c1.parent = c2.parent and c1.size = c2.size and c1.name < c2.name;


-- Q4: Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
	with dogsInStack (names, total, n, max) as(
		select name, height, 1, height from dogs union
		select stack.names || ", " || d.name, total+d.height, n+1, d.height
			from dogsInStack as stack, dogs as d
			where stack.max < d.height and n < 4
	)

  	select names, total
  	from dogsInStack
  	where total >= 170 and n=4
  	order by total
  ;