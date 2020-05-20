namespace com.halffulldata.models
{
    public class LastModifiedUtc
    {
        public string ISO8601Date { get; set; }
    }

    public class FirstModifiedUtc
    {
        public string ISO8601Date { get; set; }
    }

    public class Company
    {
        public string Id { get; set; }
        public string Name { get; set; }
    }

    public class UserProfileModel
    {
        public string Gamertag { get; set; }
        public LastModifiedUtc LastModifiedUtc { get; set; }
        public FirstModifiedUtc FirstModifiedUtc { get; set; }
        public string ServiceTag { get; set; }
        public Company Company { get; set; }
    }
}