namespace com.halffulldata.models
{
    public class BaseAuth
    {
        public string Key { get; set; }
        public string Value { get; set; }
    }

    public class ApiBasePath
    {
        public string Name { get; set; }
        public string Url { get; set; }
    }

    public class Endpoints
    {
        public string Profile { get; set; }
    }

    public class Constants
    {

    }

    public class ApiConfigOptions
    {
        public BaseAuth BaseAuth {get; set;}
        public ApiBasePath ApiBasePath { get; set; }
        public Endpoints Endpoints { get; set; }
        public Constants Constants { get; set; }
    }
}