using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.AspNetCore.Http;
using System;
using System.IO;
using com.halffulldata.models;
using com.halffulldata.services;

namespace com.halffulldata.api
{
    public class Startup
    {
        private readonly IConfiguration _config;

        public Startup(IWebHostEnvironment env)
        {
            // Get our develop vs production config
            var builder = new ConfigurationBuilder()
            .SetBasePath(env.ContentRootPath)
            .AddJsonFile($"appsettings.json", optional: false)
            .AddEnvironmentVariables();

            this._config = builder.Build();
        }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddOptions<ApiConfigOptions>().Bind(_config.GetSection("ApiConfig"));
            var apiConfig = _config.GetSection("ApiConfig").Get<ApiConfigOptions>();
            // services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
            //     .AddJwtBearer(cfg =>
            //     {
            //         cfg.Events = new JwtBearerEvents
            //         {
            //             OnMessageReceived = context =>
            //             {
            //                 context.Token = context.Request.Cookies["access_token"];
            //                 return Task.CompletedTask;
            //             }
            //         };
            //         cfg.TokenValidationParameters = new TokenValidationParameters()
            //         {
            //             ValidIssuer = _config["AuthSettings:validIssuer"],
            //             ValidAudience = _config["AuthSettings:validAudience"],
            //             IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_config["AuthSettings:secretKey"]))
            //         };
            //     }
            //     );
            // services.AddAuthorization(opt =>
            // {
            //     opt.AddPolicy("AdminUser", policy => { policy.RequireClaim("UserRole", "admin"); });
            // });
            services.AddControllersWithViews()
                .SetCompatibilityVersion(CompatibilityVersion.Version_3_0)
                .AddNewtonsoftJson(options => options.SerializerSettings.ReferenceLoopHandling = Newtonsoft.Json.ReferenceLoopHandling.Ignore);
            services.AddHttpClient(apiConfig.ApiBasePath.Name, c =>
            {
                c.BaseAddress = new Uri(apiConfig.ApiBasePath.Url);
                c.DefaultRequestHeaders.Add(apiConfig.BaseAuth.Key, apiConfig.BaseAuth.Value);
            });
            services.AddSingleton<IApiService, ApiService>();
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            app.UseHttpsRedirection();
            app.UseStaticFiles();
            app.UseRouting();
            app.UseAuthentication();
            app.UseAuthorization();
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });

            app.Run(async (context) =>
            {
                context.Response.ContentType = "text/html";
                await context.Response.SendFileAsync(Path.Combine(env.WebRootPath, "index.html"));
            });
        }
    }
}
