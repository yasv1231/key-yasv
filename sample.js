// 示例JavaScript文件
function greet(name) {
    return `Hello, ${name}!`;
}

function calculateSum(a, b) {
    return a + b;
}

// 导出函数
module.exports = {
    greet,
    calculateSum
};

// 使用示例
console.log(greet("World"));
console.log("Sum:", calculateSum(5, 3));
