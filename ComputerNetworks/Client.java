import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        String hostname = "localhost";
        int port = 5000;

        try (Socket socket = new Socket(hostname, port)) {
            System.out.println("Connected to the server.");

            // Input and Output Streams
            OutputStream output = socket.getOutputStream();
            PrintWriter writer = new PrintWriter(output, true);

            InputStream input = socket.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(input));

            // Sending messages to server
            BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
            String message;

            do {
                System.out.print("Enter message: ");
                message = userInput.readLine();
                writer.println(message);

                String serverResponse = reader.readLine();
                System.out.println("Server: " + serverResponse);
            } while (!message.equalsIgnoreCase("bye"));

            System.out.println("Disconnected from server.");

        } catch (UnknownHostException ex) {
            System.out.println("Server not found: " + ex.getMessage());
        } catch (IOException ex) {
            System.out.println("I/O error: " + ex.getMessage());
        }
    }
}