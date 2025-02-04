using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();

// Habilitar CORS
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowReactApp",
        policy =>
        {
            policy.WithOrigins("http://localhost:9999","http://localhost:3000","http://web:9999","http://web:3000") // Cambia a la URL de tu frontend
                  .AllowAnyMethod()
                  .AllowAnyHeader()
                  .AllowCredentials();
        });
});

// Add YARP (Reverse Proxy) service
builder.Services.AddReverseProxy()
    .LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"));

var app = builder.Build();

// app.UseAuthorization();
// app.MapControllers();
app.UseCors("AllowReactApp");

// Use YARP middleware to handle reverse proxying
app.MapReverseProxy();

app.Run();
