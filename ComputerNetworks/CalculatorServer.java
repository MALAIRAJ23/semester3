
import java.io.*;
import java.net.*;

public class CalculatorServer {
    public static void main(String[] args) {
        int port = 5000;
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Calculator Server is running...");
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected.");
                new ClientHandler(clientSocket).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class ClientHandler extends Thread {
    private Socket clientSocket;
    public ClientHandler(Socket socket) {
        this.clientSocket = socket;
    }
    public void run() {
        try (
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
        ) {
            String expression;
            while ((expression = in.readLine()) != null) {
                if (expression.equalsIgnoreCase("exit")) {
                    System.out.println("Client disconnected.");
                    break;
                }
                System.out.println("Received: " + expression);
                String result = calculate(expression);
                out.println(result);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                clientSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    private static String calculate(String expression) {
        try {
            String[] tokens = expression.split(" ");
            if (tokens.length != 3) {
                return "Invalid format. Use: operand operator operand (e.g., 10 + 5)";
            }
            double num1 = Double.parseDouble(tokens[0]);
            double num2 = Double.parseDouble(tokens[2]);
            String operator = tokens[1];
            double result;
            switch (operator) {
                case "+":
                    result = num1 + num2;
                    break;
                case "-":
                    result = num1 - num2;
                    break;
                case "*":
                    result = num1 * num2;
                    break;
                case "/":
                    if (num2 == 0) return "Error: Division by zero";
                    result = num1 / num2;
                    break;
                default:
                    return "Error: Unsupported operator";
            }
            return "Result: " + result;
        } catch (NumberFormatException e) {
            return "Error: Invalid numbers";
        }
    }
}