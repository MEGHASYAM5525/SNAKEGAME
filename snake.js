// Game variables
let canvas = document.getElementById('gameCanvas');
let ctx = canvas.getContext('2d');
let box = 20;
let snake = [];
snake[0] = { x: 15 * box, y: 15 * box };

let food = {
    x: Math.floor(Math.random() * 29 + 1) * box,
    y: Math.floor(Math.random() * 29 + 1) * box
};

let direction;
let score = 0;
let highScore = 0;

// Listen for keyboard input to change direction
document.addEventListener('keydown', changeDirection);

function changeDirection(event) {
    if (event.keyCode === 37 && direction !== 'right') {
        direction = 'left';
    } else if (event.keyCode === 38 && direction !== 'down') {
        direction = 'up';
    } else if (event.keyCode === 39 && direction !== 'left') {
        direction = 'right';
    } else if (event.keyCode === 40 && direction !== 'up') {
        direction = 'down';
    }
}

// Function to draw the game
function drawGame() {
    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw the snake
    for (let i = 0; i < snake.length; i++) {
        ctx.fillStyle = (i === 0) ? 'black' : 'grey';
        ctx.fillRect(snake[i].x, snake[i].y, box, box);
    }

    // Draw the food
    ctx.fillStyle = 'red';
    ctx.fillRect(food.x, food.y, box, box);

    // Move the snake
    let snakeX = snake[0].x;
    let snakeY = snake[0].y;

    if (direction === 'left') snakeX -= box;
    if (direction === 'right') snakeX += box;
    if (direction === 'up') snakeY -= box;
    if (direction === 'down') snakeY += box;

    // Check for collision with the food
    if (snakeX === food.x && snakeY === food.y) {
        score += 10;
        if (score > highScore) highScore = score;

        // Generate new food
        food = {
            x: Math.floor(Math.random() * 29 + 1) * box,
            y: Math.floor(Math.random() * 29 + 1) * box
        };
    } else {
        // Remove the last part of the snake if no food is eaten
        snake.pop();
    }

    // Add new head to the snake
    let newHead = { x: snakeX, y: snakeY };

    // Check for collision with walls
    if (snakeX < 0 || snakeY < 0 || snakeX >= canvas.width || snakeY >= canvas.height || collision(newHead, snake)) {
        clearInterval(game);
        alert('Game Over!');
    }

    snake.unshift(newHead);

    // Display the score
    ctx.fillStyle = 'white';
    ctx.font = '24px Courier';
    ctx.fillText('Score: ' + score + '  High Score: ' + highScore, 10, 25);
}

// Function to check for collisions with the snake itself
function collision(head, array) {
    for (let i = 0; i < array.length; i++) {
        if (head.x === array[i].x && head.y === array[i].y) {
            return true;
        }
    }
    return false;
}

// Call the game loop
let game = setInterval(drawGame, 100);
