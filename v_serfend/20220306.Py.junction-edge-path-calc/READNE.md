1、junctions_result表里面应该只有key=0的节点的结果，且值为5，就是现在空白的result里面应该全部是5 



2、key=1的节点的结果应该已经转化为新生成的边的值了，在edge_result里，但是现在edge_result只有原来的47条路段的结果 



3、以id=1的节点为例，输出的结果应该是全部四个进口，每个进口三个转向，一共12个值 ，且输出的结果应该是新生成的edge的属性 



> 考虑到输出的结果会有6个、12个，所以目前Junction表中的输出是没有展开的输出，只记录direction id和junction id以及result=Ti(d)这三个值 使用direction id可以获取到当前节点的所有转向edgeM（1-4个）-directionN（0-3个），从而得到0-12个结果 



再就是edge表的结果需要加上s_id，e_id，dir三列 

> （已修正完成） 

