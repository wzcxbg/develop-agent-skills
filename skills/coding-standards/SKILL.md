---
name: coding-standards
description: 通用编码规范技能。当用户请求生成代码时，生成的代码请遵循当前规范。
---

# 通用编码规范

本技能旨在提供一套通用的编码规范和最佳实践，以提升代码的可读性、可维护性和健壮性。

## 1. 异常处理 (Exception Handling)

*   **避免过度捕获**：在开发阶段，尽量不要捕获异常，而是让异常抛出并暴露问题，从而修复潜在的 Bug。
*   **精确捕获**：永远不要为了方便而捕获顶层异常（如 `Exception` 或 `Throwable`）。只有在确切知道某块代码在特定极端情况下会抛出特定异常，且该异常可以被合理处理时，才去捕获该特定类型的异常。

## 2. 注释规范 (Comments)

*   **自解释代码**：代码本身应该是最好的文档。
*   **注释功能**：如果要加注释，应该优先使用方法、类级别的注释，而不是在方法内写行内注释。

## 3. 函数式编程与链式调用 (Functional & Chaining)

*   **优先使用链式调用**：对于集合操作、流处理等场景，优先使用函数式编程和链式调用。
    *   *示例*：获取所有班级中平均分超过 90 分的学生：
        ```java
        classes.flatMap(class -> class.students)
               .filter(student -> student.score > 90)
               .toList()
        ```
*   **避免滥用**：如果链式调用只有一个节点，且无法一行写完时，请不要使用链式写法，而应使用原生循环。
    *   *示例*：遍历学生列表，为每个学生生成报告并发送邮件：
    *   *反例*：
        ```java
        students.forEach(student -> {
            String report = generateReport(student);
            sendEmail(student.email, report);
        });
        ```
    *   *正例*：
        ```java
        for (Student student : students) {
            String report = generateReport(student);
            sendEmail(student.email, report);
        }
        ```

## 4. 卫语句与控制流 (Guard Clauses & Control Flow)

*   **减少嵌套**：尽量减少 `if-else` 的深层嵌套，保持代码扁平化。建议嵌套层级不超过 3 层。
*   **使用卫语句**：优先使用“卫语句”（Guard Clauses）提前处理异常或边缘情况并返回，避免后续核心逻辑包裹在 `else` 块中。
    *   *示例*：
        ```java
        if (input == null) {
            return;
        }
        // Core logic here...
        ```
*   **时间驱动等待**：在实现等待或轮询逻辑时，优先使用“超时时间 + 轮询间隔”的机制，而非简单的“循环 N 次”。时间语义更清晰，且易于调整和配置。

## 5. 不可变性 (Immutability)

*   **优先不可变**：优先使用不可变对象和变量。
    *   Java: 使用 `final`
    *   Kotlin: 使用 `val`
    *   JS/TS: 使用 `const`
*   **限制可变性**：只有在确有必要修改变量值时，才使用可变类型（如 `var` 或非 `final` 变量）。
*   **纯函数**：尽量避免副作用，函数的输出应仅依赖于输入参数，而不修改外部状态。

## 6. 日志规范 (Logging)

*   **禁止标准输出**：生产环境代码中严禁使用 `System.out.println`、`console.log` 或 `print` 等标准输出语句。
*   **日志工具**：优先复用项目现有日志工具封装，或使用成熟的日志框架。

## 7. 方法设计与复杂度 (Method Design)

*   **单一职责原则 (SRP)**：一个方法应该只做一件事，并把它做好。如果方法承担过多职责，应拆分为多个小方法。
*   **控制长度**：尽量保持方法简短，建议不超过 50 行。长方法难以阅读和维护。
*   **限制参数数量**：方法参数数量尽量控制在 4 个以内。如果参数过多，考虑引入参数对象（Parameter Object）或使用 Builder 模式。
*   **降低圈复杂度**：避免过深的嵌套和过于复杂的逻辑分支。若逻辑复杂，尝试提取子方法或使用策略模式。
*   **消除重复 (DRY)**：遵循“不要重复自己”（Don't Repeat Yourself）原则。若同一类逻辑在多处出现，应提取为统一的辅助方法或类，以减少重复代码并降低维护成本。
*   **扁平化调用**：避免不必要的中间层封装。如果中间函数仅是简单的透传，应直接调用目标方法。保持调用链简短有助于提高代码可读性和调试效率。

## 8. 类型安全与返回值 (Type Safety & Return Values)

*   **显式表达“无结果”**：当方法可能不返回结果时，应使用显式的类型（如 C++ `std::optional<T>`, Java `Optional<T>`, Rust `Option<T>`）来表达，迫使调用方处理空值情况，避免隐式返回 null 导致空指针异常。

## 9. 命名规范 (Naming Conventions)

*   **统一行为命名**：对于具有相同语义的行为，应使用统一的 API 名称（如 `Attach`, `Open`），并通过参数重载来区分不同的输入源。保持接口一致性，减少认知负担。

## 10. 单元测试 (Unit Testing)

*   **覆盖率**：核心业务逻辑的单元测试覆盖率应达到 80% 以上。
*   **独立性**：单元测试必须独立，不依赖外部环境（数据库、网络等）。
*   **命名规范**：测试方法名应清晰描述测试场景和预期结果。
    *   *示例*：`shouldReturnTrueWhenInputIsValid`
*   **清晰断言**：使用表达力强的断言库。
    *   *反例*：`assertTrue(result == expected)`
    *   *正例*：`assertThat(result).isEqualTo(expected)`

## 11. 构建与验证 (Build & Verification)

*   **本地构建**：完成代码编写后，仅当识别到构建系统支持默认构建目录或共享缓存（如 Gradle, Maven, npm）时，尝试执行构建以验证代码；对于需手动指定构建目录的系统（如 CMake），为避免重复构建浪费资源，应跳过自动编译。
*   **编译检查**：确保代码能够成功编译通过。严禁提交无法编译的代码。
