public class HelloWorld {
    public static void main(String[] args) {
        String variableName = args.length > 0 ? args[0] : "java";
        String variableValue = System.getenv(variableName);

        System.out.println("Hello, World!");
        System.out.println(variableName + "=" + variableValue);
    }
}
