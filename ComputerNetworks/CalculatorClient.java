
import java.io.*;
import java.net.*;

public class CalculatorClient {
    public static void main(String[] args) {
        String serverAddress = "localhost";
        int port = 5000;
        try (Socket socket = new Socket(serverAddress, port);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in))) {
            System.out.println("Connected to Calculator Server.");
            System.out.println("Enter arithmetic expressions (e.g., 10 + 5). Type 'exit' to quit.");
            while (true) {
                System.out.print("Enter expression: ");
                String expression = userInput.readLine();
                if (expression.equalsIgnoreCase("exit")) {
                    out.println("exit");
                    System.out.println("Disconnected from server.");
                    break;
                }
                out.println(expression);
                String result = in.readLine();
                System.out.println("Server response: " + result);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}