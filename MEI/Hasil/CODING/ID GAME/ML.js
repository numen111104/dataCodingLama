OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api-xyz.com/trueid/mobilelegends/?id=960207848&zone=12821")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();