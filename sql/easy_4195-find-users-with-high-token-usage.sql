# Write your MySQL query statement below
WITH UserStats AS (
    SELECT 
        user_id,
        tokens,
        COUNT(*) OVER(PARTITION BY user_id) as prompt_count,
        AVG(tokens) OVER(PARTITION BY user_id) as avg_tokens
    FROM prompts
)
SELECT 
    user_id, 
    prompt_count, 
    ROUND(avg_tokens, 2) AS avg_tokens
FROM UserStats
WHERE prompt_count >= 3
GROUP BY user_id, prompt_count, avg_tokens
HAVING MAX(tokens) > avg_tokens
ORDER BY avg_tokens DESC, user_id ASC;