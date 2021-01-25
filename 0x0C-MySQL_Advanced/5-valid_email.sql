-- Creates a trigger that resets the attribute of valid_email after email changed .
DELIMITER $$
CREATE TRIGGER valid_email
BEFORE UPDATE ON users FOR EACH ROW
BEGIN IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0; END IF;
END$$
