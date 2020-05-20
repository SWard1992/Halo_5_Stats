using System;
using System.Net.Http;
using System.Threading.Tasks;
using com.halffulldata.models;
using Microsoft.Extensions.Options;
using Newtonsoft.Json;

namespace com.halffulldata.services
{
    public class ApiService : IApiService
    {
        private readonly IHttpClientFactory _clientFactory;
        private readonly ApiConfigOptions _apiConfigOptions;
        public ApiService(IHttpClientFactory clientFactory, IOptions<ApiConfigOptions> apiConfigOptions)
        {
            _clientFactory = clientFactory;
            _apiConfigOptions = apiConfigOptions.Value;
        }
        public async Task<UserProfileModel> GetUserProfile(string userId)
        {
            try
            {
                HttpClient client = _clientFactory.CreateClient(_apiConfigOptions.ApiBasePath.Name);

                HttpResponseMessage response = await client.GetAsync(String.Format(_apiConfigOptions.Endpoints.Profile, userId));

                string content = await response.Content.ReadAsStringAsync();

                if (response.IsSuccessStatusCode)
                {
                    return JsonConvert.DeserializeObject<UserProfileModel>(content);
                }
            }
            catch (Exception)
            {
                throw;
            }

            return null;
        }
    }
}