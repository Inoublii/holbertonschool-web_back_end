-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users SET average_score = (
	SELECT SUM(b.weight * a.score) / SUM(b.weight) FROM corrections AS x
    RIGHT JOIN projects AS b ON a.project_id = b.id WHERE a.user_id = users.id
    );
END//
