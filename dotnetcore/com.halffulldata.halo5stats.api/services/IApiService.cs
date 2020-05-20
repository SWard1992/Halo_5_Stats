using System.Threading.Tasks;
using com.halffulldata.models;

namespace com.halffulldata.services
{
    public interface IApiService
    {
        Task<UserProfileModel> GetUserProfile(string userId);
    }
}