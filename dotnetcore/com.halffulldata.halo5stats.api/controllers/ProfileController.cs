using System;
using System.Threading.Tasks;
using com.halffulldata.services;
using Microsoft.AspNetCore.Mvc;

namespace com.halffulldata.controllers
{
    [Route("api/[controller]")]
    public class ProfileController : Controller
    {
        private readonly IApiService _apiService;
        public ProfileController(IApiService apiService)
        {
            _apiService = apiService;
        }

        [HttpGet("{user}")]
        public async Task<IActionResult> GetUserProfile(string user)
        {
            try
            {
                var userProfile = await _apiService.GetUserProfile(user);
                return Ok(userProfile);
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }

        }
    }
}