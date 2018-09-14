CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name, b.size from dogs as a, sizes as b where a.height > b.min and a.height <= b.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT a.name from dogs as a, parents as b, dogs as c where a.name = b.child and b.parent = c.name order by -c.height;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT a.name || ' and ' || b.name || ' are ' || a.size || ' siblings' as sentence from size_of_dogs as a, size_of_dogs as b, parents as c, parents as d where a.size = b.size and a.name = c.child and b.name = d.child and c.parent = d.parent and a.name < b.name;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks AS
  with helper(names, num_dog, last_height, total_height) as (
    select name, 1, height, height from dogs union
    select names || ', ' || name, num_dog + 1, height, total_height + height from helper, dogs where last_height < height and num_dog < 4
    )
    select names, total_height from helper where total_height >= 170 order by total_height;
