-- =========================
-- SEARCH FUNCTION
-- =========================
CREATE OR REPLACE FUNCTION search_contacts(p TEXT)
RETURNS TABLE(first_name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.first_name, c.phone
    FROM contacts c
    WHERE c.first_name ILIKE '%' || p || '%'
       OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


-- =========================
-- PAGINATION FUNCTION
-- =========================
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(first_name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.first_name, c.phone
    FROM contacts c
    ORDER BY c.first_name
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;