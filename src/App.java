import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;

public class WorkerApiExample {
    
    private static final String API_ENDPOINT = "https://<your_worker_api_endpoint>";
    private static final String AUTHORIZATION_HEADER = "Authorization";
    private static final String BEARER_PREFIX = "Bearer ";
    private static final String ACCESS_TOKEN = "<your_access_token>";

    public static void main(String[] args) throws IOException {
        
        URL url = new URL(API_ENDPOINT);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestProperty(AUTHORIZATION_HEADER, BEARER_PREFIX + ACCESS_TOKEN);
        connection.setRequestMethod("POST");
        
        if (connection.getResponseCode() == 200) {
            // Handle successful API call
            System.out.println("API call succeeded.");
        } else {
            // Handle failed API call
            System.out.println("API call failed with status code " + connection.getResponseCode() + ": " + connection.getResponseMessage());
        }
        
        connection.disconnect();
    }
}
