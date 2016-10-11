// Generated by gencpp from file tum_ardrone/SetMaxControl.msg
// DO NOT EDIT!


#ifndef TUM_ARDRONE_MESSAGE_SETMAXCONTROL_H
#define TUM_ARDRONE_MESSAGE_SETMAXCONTROL_H

#include <ros/service_traits.h>


#include <tum_ardrone/SetMaxControlRequest.h>
#include <tum_ardrone/SetMaxControlResponse.h>


namespace tum_ardrone
{

struct SetMaxControl
{

typedef SetMaxControlRequest Request;
typedef SetMaxControlResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetMaxControl
} // namespace tum_ardrone


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::tum_ardrone::SetMaxControl > {
  static const char* value()
  {
    return "7ff7215b2a764d7df902316cc8f39be9";
  }

  static const char* value(const ::tum_ardrone::SetMaxControl&) { return value(); }
};

template<>
struct DataType< ::tum_ardrone::SetMaxControl > {
  static const char* value()
  {
    return "tum_ardrone/SetMaxControl";
  }

  static const char* value(const ::tum_ardrone::SetMaxControl&) { return value(); }
};


// service_traits::MD5Sum< ::tum_ardrone::SetMaxControlRequest> should match 
// service_traits::MD5Sum< ::tum_ardrone::SetMaxControl > 
template<>
struct MD5Sum< ::tum_ardrone::SetMaxControlRequest>
{
  static const char* value()
  {
    return MD5Sum< ::tum_ardrone::SetMaxControl >::value();
  }
  static const char* value(const ::tum_ardrone::SetMaxControlRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::tum_ardrone::SetMaxControlRequest> should match 
// service_traits::DataType< ::tum_ardrone::SetMaxControl > 
template<>
struct DataType< ::tum_ardrone::SetMaxControlRequest>
{
  static const char* value()
  {
    return DataType< ::tum_ardrone::SetMaxControl >::value();
  }
  static const char* value(const ::tum_ardrone::SetMaxControlRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::tum_ardrone::SetMaxControlResponse> should match 
// service_traits::MD5Sum< ::tum_ardrone::SetMaxControl > 
template<>
struct MD5Sum< ::tum_ardrone::SetMaxControlResponse>
{
  static const char* value()
  {
    return MD5Sum< ::tum_ardrone::SetMaxControl >::value();
  }
  static const char* value(const ::tum_ardrone::SetMaxControlResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::tum_ardrone::SetMaxControlResponse> should match 
// service_traits::DataType< ::tum_ardrone::SetMaxControl > 
template<>
struct DataType< ::tum_ardrone::SetMaxControlResponse>
{
  static const char* value()
  {
    return DataType< ::tum_ardrone::SetMaxControl >::value();
  }
  static const char* value(const ::tum_ardrone::SetMaxControlResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // TUM_ARDRONE_MESSAGE_SETMAXCONTROL_H
