-- this creates a stored an index idx_name_first on the table names and the first letter of name
CREATE INDEX idx_name_first_score
ON names (name(1), score);
