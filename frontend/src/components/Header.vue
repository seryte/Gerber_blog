<template>
    <div class="headBox">
        <el-menu
                :default-active="activeIndex2"
                class="el-menu-demo"
                mode="horizontal"
                @select="handleSelect"
                background-color="#545c64"
                text-color="#fff"
                active-text-color="#ffd04b">
            <el-menu-item index="1">博客首页</el-menu-item>
            <el-submenu index="2">
                <template slot="title">分类</template>
                <el-menu-item index="2-1">Python</el-menu-item>
                <el-menu-item index="2-2">Javascript</el-menu-item>
                <el-menu-item index="2-3">Go</el-menu-item>
                <el-submenu index="2-4">
                    <template slot="title">科学上网</template>
                    <el-menu-item index="2-4-1">选项1</el-menu-item>
                    <el-menu-item index="2-4-2">选项2</el-menu-item>
                    <el-menu-item index="2-4-3">选项3</el-menu-item>
                </el-submenu>
            </el-submenu>
            <el-menu-item index="3">留言板</el-menu-item>
            <el-menu-item index="4"><a href="javascript:void(0)">关于我</a></el-menu-item>

                <el-menu-item index="5"><a href="javascript:void(0);" @click="logoinFun(1)">登录&nbsp;</a>|<a
                        href="javascript:void(0);"
                        @click="logoinFun(0)">&nbsp;注册</a>
                </el-menu-item>
                <el-menu-item class="pcsearchinput">
                    <el-input placeholder="搜索" icon="search">
                    </el-input>
                </el-menu-item>


        </el-menu>

    </div>

</template>

<script>
    export default {
        data() {
            return {
                activeIndex: '1',
                activeIndex2: '1'
            };
        },
        methods: {
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            }
        }
    }
</script>
<style scoped>
    .headBox li.is-active {
        background: #48456C;
        background: rgba(73, 69, 107, 0.7);
    }
    .headBox .pcsearchbox {
	padding: 0;
	max-width: 170px;
	/*min-width: 30px;*/
	height: 100%;
	line-height: 38px;
	position: absolute;
	top: 0;
	right: 0;
	cursor: pointer;
}
</style>
