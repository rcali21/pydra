from ..graph import MyGraph
import pytest


def test_no_edges():
    """a, b"""
    graph = MyGraph(nodes=["a", "b"])
    assert graph.nodes == ["a", "b"]
    assert graph.edges == []


def test_edges_1():
    """a -> b"""
    graph = MyGraph(nodes=["a", "b"], edges=[("a", "b")])
    assert graph.nodes == ["a", "b"]
    assert graph.edges == [("a", "b")]


def test_edges_2():
    """a -> b"""
    graph = MyGraph(nodes=["b", "a"], edges=[("a", "b")])
    assert graph.nodes == ["b", "a"]
    assert graph.edges == [("a", "b")]


def test_edges_3():
    """a-> b -> c; a -> c; d"""
    graph = MyGraph(
        nodes=["b", "a", "c", "d"], edges=[("a", "b"), ("b", "c"), ("a", "c")]
    )
    assert graph.nodes == ["b", "a", "c", "d"]
    assert graph.edges == [("a", "b"), ("b", "c"), ("a", "c")]


def test_edges_ecxeption_1():
    with pytest.raises(Exception) as excinfo:
        graph = MyGraph(nodes=["a", "b", "a"], edges=[("a", "b")])
    assert "repeated elements" in str(excinfo.value)


def test_edges_ecxeption_2():
    with pytest.raises(Exception) as excinfo:
        graph = MyGraph(nodes=["a", "b"], edges=[("a", "c")])
    assert "can't be added" in str(excinfo.value)


def test_sort_1():
    """a -> b"""
    graph = MyGraph(nodes=["a", "b"], edges=[("a", "b")])
    assert graph.nodes == ["a", "b"]
    assert graph.edges == [("a", "b")]

    graph.sorting()
    assert graph.sorted_nodes == ["a", "b"]


def test_sort_2():
    """a -> b"""
    graph = MyGraph(nodes=["b", "a"], edges=[("a", "b")])
    assert graph.nodes == ["b", "a"]
    assert graph.edges == [("a", "b")]

    graph.sorting()
    assert graph.sorted_nodes == ["a", "b"]


def test_sort_3():
    """a-> b -> c; a -> c; d"""
    graph = MyGraph(
        nodes=["b", "a", "c", "d"], edges=[("a", "b"), ("b", "c"), ("a", "c")]
    )
    assert graph.nodes == ["b", "a", "c", "d"]
    assert graph.edges == [("a", "b"), ("b", "c"), ("a", "c")]

    graph.sorting()
    assert graph.sorted_nodes == ["a", "d", "b", "c"]


def test_sort_4():
    """a-> b -> c; a -> c; a -> d"""
    graph = MyGraph(
        nodes=["b", "a", "c", "d"],
        edges=[("a", "b"), ("b", "c"), ("a", "c"), ("a", "d")],
    )
    assert graph.nodes == ["b", "a", "c", "d"]
    assert graph.edges == [("a", "b"), ("b", "c"), ("a", "c"), ("a", "d")]

    graph.sorting()
    assert graph.sorted_nodes == ["a", "b", "d", "c"]


def test_sort_5():
    """a-> b -> c; a -> c; d -> c"""
    graph = MyGraph(
        nodes=["b", "a", "c", "d"],
        edges=[("a", "b"), ("b", "c"), ("a", "c"), ("d", "c")],
    )
    assert graph.nodes == ["b", "a", "c", "d"]
    assert graph.edges == [("a", "b"), ("b", "c"), ("a", "c"), ("d", "c")]

    graph.sorting()
    assert graph.sorted_nodes == ["a", "d", "b", "c"]


def test_sort_6():
    """a -> b -> c -> e; a -> c -> e; a -> b -> d -> e"""
    graph = MyGraph(
        nodes=["d", "e", "c", "b", "a"],
        edges=[("a", "b"), ("b", "c"), ("a", "c"), ("b", "d"), ("c", "e"), ("d", "e")],
    )
    assert graph.nodes == ["d", "e", "c", "b", "a"]
    assert graph.edges == [
        ("a", "b"),
        ("b", "c"),
        ("a", "c"),
        ("b", "d"),
        ("c", "e"),
        ("d", "e"),
    ]

    graph.sorting()
    assert graph.sorted_nodes == ["a", "b", "d", "c", "e"]


def test_remove_1():
    """a -> b"""
    graph = MyGraph(nodes=["a", "b"], edges=[("a", "b")])
    assert graph.nodes == ["a", "b"]
    assert graph.edges == [("a", "b")]

    graph.sorting()
    assert graph.sorted_nodes == ["a", "b"]

    # removing a node (e.g. after is sent to run)
    graph.removing("a")
    assert graph.nodes == ["b"]
    assert graph.edges == []
    assert graph.sorted_nodes == ["b"]


def test_remove_2():
    """a-> b -> c; a -> c; d"""
    graph = MyGraph(
        nodes=["b", "a", "c", "d"], edges=[("a", "b"), ("b", "c"), ("a", "c")]
    )
    assert graph.nodes == ["b", "a", "c", "d"]
    assert graph.edges == [("a", "b"), ("b", "c"), ("a", "c")]

    graph.sorting()
    assert graph.sorted_nodes == ["a", "d", "b", "c"]

    graph.removing("a")
    assert graph.nodes == ["b", "c", "d"]
    assert graph.edges == [("b", "c")]
    assert graph.sorted_nodes == ["d", "b", "c"]


def test_remove_3():
    """a-> b -> c; a -> c; d"""
    graph = MyGraph(
        nodes=["b", "a", "c", "d"], edges=[("a", "b"), ("b", "c"), ("a", "c")]
    )
    assert graph.nodes == ["b", "a", "c", "d"]
    assert graph.edges == [("a", "b"), ("b", "c"), ("a", "c")]

    graph.sorting()
    assert graph.sorted_nodes == ["a", "d", "b", "c"]

    graph.removing("d")
    assert graph.nodes == ["b", "a", "c"]
    assert graph.edges == [("a", "b"), ("b", "c"), ("a", "c")]
    assert graph.sorted_nodes == ["a", "b", "c"]


def test_remove_4():
    """ a-> b -> c; a -> d -> e"""
    graph = MyGraph(
        nodes=["b", "a", "c", "d", "e"],
        edges=[("a", "b"), ("b", "c"), ("a", "d"), ("d", "e")],
    )
    assert graph.nodes == ["b", "a", "c", "d", "e"]
    assert graph.edges == [("a", "b"), ("b", "c"), ("a", "d"), ("d", "e")]

    graph.sorting()
    assert graph.sorted_nodes == ["a", "b", "d", "c", "e"]

    graph.removing("a")
    assert graph.nodes == ["b", "c", "d", "e"]
    assert graph.edges == [("b", "c"), ("d", "e")]
    assert graph.sorted_nodes == ["b", "d", "c", "e"]

    graph.removing("d")
    assert graph.nodes == ["b", "c", "e"]
    assert graph.edges == [("b", "c")]
    assert graph.sorted_nodes == ["b", "e", "c"]


def test_remove_exception_1():
    """a -> b"""
    graph = MyGraph(nodes=["a", "b"], edges=[("a", "b")])
    assert graph.nodes == ["a", "b"]
    assert graph.edges == [("a", "b")]

    graph.sorting()
    assert graph.sorted_nodes == ["a", "b"]

    with pytest.raises(Exception) as excinfo:
        graph.removing("b")
    assert "has to wait" in str(excinfo.value)
