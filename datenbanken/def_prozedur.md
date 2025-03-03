CREATE OR REPLACE PROCEDURE populate_testtable() 
LANGUAGE PLPGSQL 
AS $BODY$ 
BEGIN 
DELETE FROM testtable; 
INSERT INTO testtable VALUES (1, 'first name'); 
INSERT INTO testtable VALUES (2, 'second name'); 
RAISE NOTICE 'populate_testtable finished successfully'; 
END; 
$BODY$; 
--invocation: 
-- CALL populate_testtable();
