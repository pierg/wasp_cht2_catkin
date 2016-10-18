; Auto-generated. Do not edit!


(cl:in-package wasp_custom_msgs-msg)


;//! \htmlinclude image_point.msg.html

(cl:defclass <image_point> (roslisp-msg-protocol:ros-message)
  ((ID
    :reader ID
    :initarg :ID
    :type cl:fixnum
    :initform 0)
   (point
    :reader point
    :initarg :point
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (width
    :reader width
    :initarg :width
    :type std_msgs-msg:Int64
    :initform (cl:make-instance 'std_msgs-msg:Int64))
   (height
    :reader height
    :initarg :height
    :type std_msgs-msg:Int64
    :initform (cl:make-instance 'std_msgs-msg:Int64)))
)

(cl:defclass image_point (<image_point>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <image_point>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'image_point)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name wasp_custom_msgs-msg:<image_point> is deprecated: use wasp_custom_msgs-msg:image_point instead.")))

(cl:ensure-generic-function 'ID-val :lambda-list '(m))
(cl:defmethod ID-val ((m <image_point>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader wasp_custom_msgs-msg:ID-val is deprecated.  Use wasp_custom_msgs-msg:ID instead.")
  (ID m))

(cl:ensure-generic-function 'point-val :lambda-list '(m))
(cl:defmethod point-val ((m <image_point>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader wasp_custom_msgs-msg:point-val is deprecated.  Use wasp_custom_msgs-msg:point instead.")
  (point m))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <image_point>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader wasp_custom_msgs-msg:width-val is deprecated.  Use wasp_custom_msgs-msg:width instead.")
  (width m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <image_point>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader wasp_custom_msgs-msg:height-val is deprecated.  Use wasp_custom_msgs-msg:height instead.")
  (height m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <image_point>) ostream)
  "Serializes a message object of type '<image_point>"
  (cl:let* ((signed (cl:slot-value msg 'ID)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'point) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'width) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'height) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <image_point>) istream)
  "Deserializes a message object of type '<image_point>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ID) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'point) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'width) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'height) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<image_point>)))
  "Returns string type for a message object of type '<image_point>"
  "wasp_custom_msgs/image_point")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'image_point)))
  "Returns string type for a message object of type 'image_point"
  "wasp_custom_msgs/image_point")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<image_point>)))
  "Returns md5sum for a message object of type '<image_point>"
  "8d6f24f08099975fe78b0257a398b6bb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'image_point)))
  "Returns md5sum for a message object of type 'image_point"
  "8d6f24f08099975fe78b0257a398b6bb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<image_point>)))
  "Returns full string definition for message of type '<image_point>"
  (cl:format cl:nil "#Custom message for publishing a point in an image and getting image data~%#image_point.msg~%int16 ID~%geometry_msgs/Point point~%std_msgs/Int64 width~%std_msgs/Int64 height~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: std_msgs/Int64~%int64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'image_point)))
  "Returns full string definition for message of type 'image_point"
  (cl:format cl:nil "#Custom message for publishing a point in an image and getting image data~%#image_point.msg~%int16 ID~%geometry_msgs/Point point~%std_msgs/Int64 width~%std_msgs/Int64 height~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: std_msgs/Int64~%int64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <image_point>))
  (cl:+ 0
     2
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'point))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'width))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'height))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <image_point>))
  "Converts a ROS message object to a list"
  (cl:list 'image_point
    (cl:cons ':ID (ID msg))
    (cl:cons ':point (point msg))
    (cl:cons ':width (width msg))
    (cl:cons ':height (height msg))
))
