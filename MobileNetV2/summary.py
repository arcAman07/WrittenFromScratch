from model import MobileNetV2 
model = MobileNetV2()
from torchvision import models
from torchsummary import summary

print(summary(model,(3,224,224)))

"""

----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1         [-1, 32, 112, 112]             864
       BatchNorm2d-2         [-1, 32, 112, 112]              64
             ReLU6-3         [-1, 32, 112, 112]               0
            Conv2d-4         [-1, 32, 112, 112]           1,024
       BatchNorm2d-5         [-1, 32, 112, 112]              64
             ReLU6-6         [-1, 32, 112, 112]               0
            Conv2d-7         [-1, 32, 112, 112]             288
       BatchNorm2d-8         [-1, 32, 112, 112]              64
             ReLU6-9         [-1, 32, 112, 112]               0
           Conv2d-10         [-1, 16, 112, 112]             512
      BatchNorm2d-11         [-1, 16, 112, 112]              32
            ReLU6-12         [-1, 16, 112, 112]               0
 LinearBottleneck-13         [-1, 16, 112, 112]               0
           Conv2d-14         [-1, 96, 112, 112]           1,536
      BatchNorm2d-15         [-1, 96, 112, 112]             192
            ReLU6-16         [-1, 96, 112, 112]               0
           Conv2d-17           [-1, 96, 56, 56]           5,184
      BatchNorm2d-18           [-1, 96, 56, 56]             192
            ReLU6-19           [-1, 96, 56, 56]               0
           Conv2d-20           [-1, 24, 56, 56]           2,304
      BatchNorm2d-21           [-1, 24, 56, 56]              48
            ReLU6-22           [-1, 24, 56, 56]               0
 LinearBottleneck-23           [-1, 24, 56, 56]               0
           Conv2d-24          [-1, 144, 56, 56]           3,456
      BatchNorm2d-25          [-1, 144, 56, 56]             288
            ReLU6-26          [-1, 144, 56, 56]               0
           Conv2d-27          [-1, 144, 56, 56]           7,776
      BatchNorm2d-28          [-1, 144, 56, 56]             288
            ReLU6-29          [-1, 144, 56, 56]               0
           Conv2d-30           [-1, 24, 56, 56]           3,456
      BatchNorm2d-31           [-1, 24, 56, 56]              48
            ReLU6-32           [-1, 24, 56, 56]               0
 LinearBottleneck-33           [-1, 24, 56, 56]               0
           Conv2d-34          [-1, 144, 56, 56]           3,456
      BatchNorm2d-35          [-1, 144, 56, 56]             288
            ReLU6-36          [-1, 144, 56, 56]               0
           Conv2d-37          [-1, 144, 28, 28]           7,776
      BatchNorm2d-38          [-1, 144, 28, 28]             288
            ReLU6-39          [-1, 144, 28, 28]               0
           Conv2d-40           [-1, 32, 28, 28]           4,608
      BatchNorm2d-41           [-1, 32, 28, 28]              64
            ReLU6-42           [-1, 32, 28, 28]               0
 LinearBottleneck-43           [-1, 32, 28, 28]               0
           Conv2d-44          [-1, 192, 28, 28]           6,144
      BatchNorm2d-45          [-1, 192, 28, 28]             384
            ReLU6-46          [-1, 192, 28, 28]               0
           Conv2d-47          [-1, 192, 28, 28]          10,368
      BatchNorm2d-48          [-1, 192, 28, 28]             384
            ReLU6-49          [-1, 192, 28, 28]               0
           Conv2d-50           [-1, 32, 28, 28]           6,144
      BatchNorm2d-51           [-1, 32, 28, 28]              64
            ReLU6-52           [-1, 32, 28, 28]               0
 LinearBottleneck-53           [-1, 32, 28, 28]               0
           Conv2d-54          [-1, 192, 28, 28]           6,144
      BatchNorm2d-55          [-1, 192, 28, 28]             384
            ReLU6-56          [-1, 192, 28, 28]               0
           Conv2d-57          [-1, 192, 28, 28]          10,368
      BatchNorm2d-58          [-1, 192, 28, 28]             384
            ReLU6-59          [-1, 192, 28, 28]               0
           Conv2d-60           [-1, 32, 28, 28]           6,144
      BatchNorm2d-61           [-1, 32, 28, 28]              64
            ReLU6-62           [-1, 32, 28, 28]               0
 LinearBottleneck-63           [-1, 32, 28, 28]               0
           Conv2d-64          [-1, 192, 28, 28]           6,144
      BatchNorm2d-65          [-1, 192, 28, 28]             384
            ReLU6-66          [-1, 192, 28, 28]               0
           Conv2d-67          [-1, 192, 14, 14]          10,368
      BatchNorm2d-68          [-1, 192, 14, 14]             384
            ReLU6-69          [-1, 192, 14, 14]               0
           Conv2d-70           [-1, 64, 14, 14]          12,288
      BatchNorm2d-71           [-1, 64, 14, 14]             128
            ReLU6-72           [-1, 64, 14, 14]               0
 LinearBottleneck-73           [-1, 64, 14, 14]               0
           Conv2d-74          [-1, 384, 14, 14]          24,576
      BatchNorm2d-75          [-1, 384, 14, 14]             768
            ReLU6-76          [-1, 384, 14, 14]               0
           Conv2d-77          [-1, 384, 14, 14]          20,736
      BatchNorm2d-78          [-1, 384, 14, 14]             768
            ReLU6-79          [-1, 384, 14, 14]               0
           Conv2d-80           [-1, 64, 14, 14]          24,576
      BatchNorm2d-81           [-1, 64, 14, 14]             128
            ReLU6-82           [-1, 64, 14, 14]               0
 LinearBottleneck-83           [-1, 64, 14, 14]               0
           Conv2d-84          [-1, 384, 14, 14]          24,576
      BatchNorm2d-85          [-1, 384, 14, 14]             768
            ReLU6-86          [-1, 384, 14, 14]               0
           Conv2d-87          [-1, 384, 14, 14]          20,736
      BatchNorm2d-88          [-1, 384, 14, 14]             768
            ReLU6-89          [-1, 384, 14, 14]               0
           Conv2d-90           [-1, 64, 14, 14]          24,576
      BatchNorm2d-91           [-1, 64, 14, 14]             128
            ReLU6-92           [-1, 64, 14, 14]               0
 LinearBottleneck-93           [-1, 64, 14, 14]               0
           Conv2d-94          [-1, 384, 14, 14]          24,576
      BatchNorm2d-95          [-1, 384, 14, 14]             768
            ReLU6-96          [-1, 384, 14, 14]               0
           Conv2d-97          [-1, 384, 14, 14]          20,736
      BatchNorm2d-98          [-1, 384, 14, 14]             768
            ReLU6-99          [-1, 384, 14, 14]               0
          Conv2d-100           [-1, 64, 14, 14]          24,576
     BatchNorm2d-101           [-1, 64, 14, 14]             128
           ReLU6-102           [-1, 64, 14, 14]               0
LinearBottleneck-103           [-1, 64, 14, 14]               0
          Conv2d-104          [-1, 384, 14, 14]          24,576
     BatchNorm2d-105          [-1, 384, 14, 14]             768
           ReLU6-106          [-1, 384, 14, 14]               0
          Conv2d-107          [-1, 384, 14, 14]          20,736
     BatchNorm2d-108          [-1, 384, 14, 14]             768
           ReLU6-109          [-1, 384, 14, 14]               0
          Conv2d-110           [-1, 96, 14, 14]          36,864
     BatchNorm2d-111           [-1, 96, 14, 14]             192
           ReLU6-112           [-1, 96, 14, 14]               0
LinearBottleneck-113           [-1, 96, 14, 14]               0
          Conv2d-114          [-1, 576, 14, 14]          55,296
     BatchNorm2d-115          [-1, 576, 14, 14]           1,152
           ReLU6-116          [-1, 576, 14, 14]               0
          Conv2d-117          [-1, 576, 14, 14]          31,104
     BatchNorm2d-118          [-1, 576, 14, 14]           1,152
           ReLU6-119          [-1, 576, 14, 14]               0
          Conv2d-120           [-1, 96, 14, 14]          55,296
     BatchNorm2d-121           [-1, 96, 14, 14]             192
           ReLU6-122           [-1, 96, 14, 14]               0
LinearBottleneck-123           [-1, 96, 14, 14]               0
          Conv2d-124          [-1, 576, 14, 14]          55,296
     BatchNorm2d-125          [-1, 576, 14, 14]           1,152
           ReLU6-126          [-1, 576, 14, 14]               0
          Conv2d-127          [-1, 576, 14, 14]          31,104
     BatchNorm2d-128          [-1, 576, 14, 14]           1,152
           ReLU6-129          [-1, 576, 14, 14]               0
          Conv2d-130           [-1, 96, 14, 14]          55,296
     BatchNorm2d-131           [-1, 96, 14, 14]             192
           ReLU6-132           [-1, 96, 14, 14]               0
LinearBottleneck-133           [-1, 96, 14, 14]               0
          Conv2d-134          [-1, 576, 14, 14]          55,296
     BatchNorm2d-135          [-1, 576, 14, 14]           1,152
           ReLU6-136          [-1, 576, 14, 14]               0
          Conv2d-137            [-1, 576, 7, 7]          31,104
     BatchNorm2d-138            [-1, 576, 7, 7]           1,152
           ReLU6-139            [-1, 576, 7, 7]               0
          Conv2d-140            [-1, 160, 7, 7]          92,160
     BatchNorm2d-141            [-1, 160, 7, 7]             320
           ReLU6-142            [-1, 160, 7, 7]               0
LinearBottleneck-143            [-1, 160, 7, 7]               0
          Conv2d-144            [-1, 960, 7, 7]         153,600
     BatchNorm2d-145            [-1, 960, 7, 7]           1,920
           ReLU6-146            [-1, 960, 7, 7]               0
          Conv2d-147            [-1, 960, 7, 7]          51,840
     BatchNorm2d-148            [-1, 960, 7, 7]           1,920
           ReLU6-149            [-1, 960, 7, 7]               0
          Conv2d-150            [-1, 160, 7, 7]         153,600
     BatchNorm2d-151            [-1, 160, 7, 7]             320
           ReLU6-152            [-1, 160, 7, 7]               0
LinearBottleneck-153            [-1, 160, 7, 7]               0
          Conv2d-154            [-1, 960, 7, 7]         153,600
     BatchNorm2d-155            [-1, 960, 7, 7]           1,920
           ReLU6-156            [-1, 960, 7, 7]               0
          Conv2d-157            [-1, 960, 7, 7]          51,840
     BatchNorm2d-158            [-1, 960, 7, 7]           1,920
           ReLU6-159            [-1, 960, 7, 7]               0
          Conv2d-160            [-1, 160, 7, 7]         153,600
     BatchNorm2d-161            [-1, 160, 7, 7]             320
           ReLU6-162            [-1, 160, 7, 7]               0
LinearBottleneck-163            [-1, 160, 7, 7]               0
          Conv2d-164            [-1, 960, 7, 7]         153,600
     BatchNorm2d-165            [-1, 960, 7, 7]           1,920
           ReLU6-166            [-1, 960, 7, 7]               0
          Conv2d-167            [-1, 960, 7, 7]          51,840
     BatchNorm2d-168            [-1, 960, 7, 7]           1,920
           ReLU6-169            [-1, 960, 7, 7]               0
          Conv2d-170            [-1, 320, 7, 7]         307,200
     BatchNorm2d-171            [-1, 320, 7, 7]             640
           ReLU6-172            [-1, 320, 7, 7]               0
LinearBottleneck-173            [-1, 320, 7, 7]               0
          Conv2d-174           [-1, 1280, 7, 7]         409,600
     BatchNorm2d-175           [-1, 1280, 7, 7]           2,560
           ReLU6-176           [-1, 1280, 7, 7]               0
       AvgPool2d-177           [-1, 1280, 1, 1]               0
          Linear-178                   [-1, 10]          12,810
================================================================
Total params: 2,557,450
Trainable params: 2,557,450
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.57
Forward/backward pass size (MB): 166.41
Params size (MB): 9.76
Estimated Total Size (MB): 176.74
----------------------------------------------------------------


"""