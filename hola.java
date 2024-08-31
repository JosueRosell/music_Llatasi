import com.google.cloud.speech.v1.RecognitionConfig;
import com.google.cloud.speech.v1.RecognitionAudio;
import com.google.cloud.speech.v1.SpeechClient;
import com.google.cloud.speech.v1.SpeechRecognitionAlternative;
import com.google.cloud.speech.v1.SpeechRecognitionResult;
import com.google.protobuf.ByteString;

import javax.sound.sampled.*;
import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class VoiceToText {

    public static void main(String[] args) throws Exception {
        String audioFilePath = "audio.wav"; // Archivo de audio temporal
        recordAudio(audioFilePath); // Graba el audio
        String text = recognizeSpeech(audioFilePath); // Reconoce el texto
        if (text != null && !text.isEmpty()) {
            writeTextLetterByLetter(text, 50); // Muestra el texto letra por letra
        }
    }

    // Graba audio desde el micrófono y guarda en un archivo WAV
    private static void recordAudio(String filePath) throws LineUnavailableException, IOException {
        AudioFormat format = new AudioFormat(16000, 16, 1, true, true);
        DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);
        TargetDataLine microphone = (TargetDataLine) AudioSystem.getLine(info);

        microphone.open(format);
        microphone.start();

        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        byte[] buffer = new byte[4096];
        int bytesRead;

        System.out.println("Grabando... (Presiona Enter para detener)");
        new Thread(() -> {
            try {
                System.in.read();
            } catch (IOException e) {
                e.printStackTrace();
            }
            microphone.stop();
            microphone.close();
        }).start();

        while (microphone.isOpen()) {
            bytesRead = microphone.read(buffer, 0, buffer.length);
            byteArrayOutputStream.write(buffer, 0, bytesRead);
        }

        Files.write(Path.of(filePath), byteArrayOutputStream.toByteArray());
        System.out.println("Grabación finalizada.");
    }

    // Reconoce el texto de un archivo de audio usando Google Cloud Speech
    private static String recognizeSpeech(String filePath) throws Exception {
        try (SpeechClient speechClient = SpeechClient.create()) {
            byte[] audioBytes = Files.readAllBytes(Path.of(filePath));
            ByteString audioData = ByteString.copyFrom(audioBytes);

            RecognitionConfig config = RecognitionConfig.newBuilder()
                    .setEncoding(RecognitionConfig.AudioEncoding.LINEAR16)
                    .setSampleRateHertz(16000)
                    .setLanguageCode("es-ES")
                    .build();
            RecognitionAudio audio = RecognitionAudio.newBuilder().setContent(audioData).build();

            SpeechRecognitionResult result = speechClient.recognize(config, audio).getResultsList().get(0);
            SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);

            System.out.println("Texto reconocido: " + alternative.getTranscript());
            return alternative.getTranscript();
        }
    }

    // Muestra el texto letra por letra con un retraso
    private static void writeTextLetterByLetter(String text, int delayMillis) throws InterruptedException {
        for (char c : text.toCharArray()) {
            System.out.print(c);
            Thread.sleep(delayMillis); // Pausa entre cada carácter
        }
    }
}
