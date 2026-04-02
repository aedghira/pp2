-- Function 1: Search records matching a pattern (name or phone)
CREATE OR REPLACE FUNCTION search_contacts_pattern(search_pattern TEXT)
RETURNS TABLE(
    id INT,
    first_name VARCHAR,
    last_name VARCHAR,
    phone_number VARCHAR,
    email VARCHAR,
    created_at TIMESTAMP
) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.last_name, p.phone_number, p.email, p.created_at
    FROM phonebook p
    WHERE p.first_name ILIKE '%' || search_pattern || '%'
       OR p.last_name ILIKE '%' || search_pattern || '%'
       OR p.phone_number ILIKE '%' || search_pattern || '%'
    ORDER BY p.first_name, p.last_name;
END;
$$ LANGUAGE plpgsql;

-- Function 2: Paginated query (LIMIT & OFFSET)
CREATE OR REPLACE FUNCTION get_contacts_paginated(limit_val INT, offset_val INT)
RETURNS TABLE(
    id INT,
    first_name VARCHAR,
    last_name VARCHAR,
    phone_number VARCHAR,
    email VARCHAR,
    created_at TIMESTAMP
) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.last_name, p.phone_number, p.email, p.created_at
    FROM phonebook p
    ORDER BY p.first_name, p.last_name
    LIMIT limit_val
    OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;