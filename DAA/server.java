package DAA;
import java.io.*;
import java.net.*;

public class server {
    public static void main(String[] args) {
        int port = 5000; // Port number for server to listen on
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server is listening on port " + port);

            Socket socket = serverSocket.accept(); // Accept client connection
            System.out.println("Client connected.");

            // Input and Output Streams
            InputStream input = socket.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(input));

            OutputStream output = socket.getOutputStream();
            PrintWriter writer = new PrintWriter(output, true);

            String message;
            while ((message = reader.readLine()) != null) {
                System.out.println("Client: " + message);
                writer.println("Server received: " + message);
                if (message.equalsIgnoreCase("bye")) {
                    break;
                }
            }

            socket.close();
            System.out.println("Client disconnected.");

        } catch (IOException ex) {
            System.out.println("Server error: " + ex.getMessage());
            ex.printStackTrace();
        }
    }
}