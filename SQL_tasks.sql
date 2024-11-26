-- Задача 1. Выведите все уникальные названия продуктов.

SELECT product_name, COUNT(*)
FROM products
GROUP BY product_name
HAVING count(*) = 1

-- Задача 2. Выведите id, название и стоимость продуктов 
-- с содержанием клетчатки (fiber) более 5 граммов.

SELECT pr.product_id, pr.product_name, pr.price
FROM products AS pr
JOIN nutritional_information AS nut
ON pr.product_id = nut.product_id
WHERE nut.fiber > 5

-- Задача 3. Выведите название продукта с самым высоким содержанием белка (protein).

SELECT product_name
FROM products AS pr
JOIN nutritional_information AS nut
ON pr.product_id = nut.product_id
ORDER BY nut.protein DESC
LIMIT 1

-- Задача 4. Подсчитайте общую сумму калорий для продуктов каждой категории, 
-- но не учитывайте продукты с нулевым жиром (fat = 0). 
-- Выведите id категории, сумму калорий.

SELECT pr.category_id, SUM(pr.calories) AS total_calories
FROM products AS pr
JOIN categories AS cat
ON pr.category_id = cat.category_id
JOIN nutritional_information as nut
ON pr.product_id = nut.product_id
WHERE nut.fat > 0
GROUP BY pr.category_id
ORDER BY pr.category_id

-- Задача 5. Рассчитайте среднюю цену товаров каждой категории. 
-- Выведите название категории, среднюю цену.

SELECT cat.category_name, ROUND(AVG(pr.price), 2) AS average_price
FROM categories AS cat
JOIN products AS pr
ON cat.category_id = pr.category_id
GROUP BY cat.category_name
ORDER BY average_price

