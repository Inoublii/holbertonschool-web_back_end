-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users SET average_score = (
	SELECT SUM(a.weight * x.score) / SUM(a.weight) FROM corrections AS x
    RIGHT JOIN projects AS a ON x.project_id = a.id WHERE x.user_id = users.id
    );
END//
