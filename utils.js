// 加载文件，返回内容
export async function load(url) {
    const response = await fetch(url);
    return await response.text();
}