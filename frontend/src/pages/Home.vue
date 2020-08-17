<template>
    <div>
        <wbc-nav></wbc-nav>
        <div class="container">
            <el-row :gutter="30">
                <el-col :sm="24" :md="16" style="transition:all .5s ease-out;margin-bottom:30px;">
<!--                    <wbc-sharelist></wbc-sharelist>-->
                </el-col>
                <el-col :sm="24" :md="8">
<!--                    <wbc-rightlist></wbc-rightlist>-->
                </el-col>
            </el-row>
        </div>
<!--        <wbc-footer></wbc-footer>-->
    </div>
</template>

<script>
    import header from "../components/header";
    import footer from "../components/footer";
    import temRightlist from "../components/temRightlist";
    import temSharelist from "../components/temSharelist";

    export default {
        name: "Home",
        data() { //选项 / 数据
            return {}
        },
        methods: { //事件处理器

        },
        components: {
            'wbc-nav': header,
            'wbc-footer': footer,
            'wbc-sharelist': temRightlist,
            'wbc-rightlist': temSharelist,
        },
        created() { //生命周期函数

        }
    }

</script>

<style>

</style>
