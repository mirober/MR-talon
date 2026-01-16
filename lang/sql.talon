title: /\.sql/
title: /.* \| psql\s*$/
-
# Commands
case when:
    "case end"
    key(left:3 enter:2 up)
when then:
    "when  then "
    key(left:6)
create table: "create table "
create view: "create view "
create index: "create index "
create synonym: "create synonym "
create procedure:
    """create proc
    as
    set nocount on;
    begin
    end
    go"""
    key(up:6 end space)
drop table: "drop table "
drop view: "drop view "
drop index: "drop index "
drop synonym: "drop synonym "
drop procedure: "drop procedure "
delete: "delete "
distinct: "distinct "
from: "from "
for system time: "for system time "
for system time all: "for system_time all"
for system time as of: "for system_time as of"
group by: "group by "
group by grouping sets:
    "group by grouping sets ()"
    key("left enter ( ) left")
having: "having "
insert into:
    "insert into "
insert into values:
    "insert into "
    key(enter:1)
    "values "
    key(up:2 end)
is not null: " is not null"
is null: " is null"
#
left join: "left join "
right join: "right join "
full join: "full join "
inner join: "inner join "
outer join: "outer join "
normal join: "join "
#
limit: "limit "
not equals: " <> "
order ascending: "asc "
order by: "order by "
order descending: "desc "
partition by: "partition by "
select every: "select * "
select count: "select count(*) "
select: "select "
set nocount on: "set nocount on"
truncate table: "truncate table "
union: "union "
union all: "union all"
update: "update"
using: "using "
value null: "null"
where: "where "
with as:
    "with  as ()"
    key(left enter:2 up:2 end left:5)
semi: key(end ;)
