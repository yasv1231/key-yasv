// Key-Yasv 主程序文件
// 这是一个演示项目，展示如何在Cursor中使用Git进行版本管理

class KeyYasv {
    constructor() {
        this.name = "Key-Yasv";
        this.version = "1.0.0";
        this.description = "Git版本管理演示项目";
    }

    // 获取项目信息
    getInfo() {
        return {
            name: this.name,
            version: this.version,
            description: this.description,
            timestamp: new Date().toISOString()
        };
    }

    // 演示功能
    demonstrate() {
        console.log("=== Key-Yasv 项目演示 ===");
        console.log("项目名称:", this.name);
        console.log("版本号:", this.version);
        console.log("描述:", this.description);
        console.log("创建时间:", new Date().toLocaleString());
        console.log("=========================");
    }

    // 计算功能
    calculate(a, b, operation = 'add') {
        switch (operation) {
            case 'add':
                return a + b;
            case 'subtract':
                return a - b;
            case 'multiply':
                return a * b;
            case 'divide':
                return b !== 0 ? a / b : 'Error: Division by zero';
            default:
                return 'Error: Invalid operation';
        }
    }
}

// 创建实例并演示
const keyYasv = new KeyYasv();

// 显示项目信息
keyYasv.demonstrate();

// 演示计算功能
console.log("\n=== 计算功能演示 ===");
console.log("5 + 3 =", keyYasv.calculate(5, 3, 'add'));
console.log("10 - 4 =", keyYasv.calculate(10, 4, 'subtract'));
console.log("6 * 7 =", keyYasv.calculate(6, 7, 'multiply'));
console.log("15 / 3 =", keyYasv.calculate(15, 3, 'divide'));

// 导出模块
if (typeof module !== 'undefined' && module.exports) {
    module.exports = KeyYasv;
}
